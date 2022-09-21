from movement import Movement
from communication import Communication
from planet import Planet
from color import Color

class Robot:

    def __init__(self):

        # current path
        self.start_x = None
        self.start_y = None
        self.start_direction = None
        self.end_x = None
        self.end_y = None
        self.end_direction = None
        self.path_status = None
        self.path_weight = None

        # current target
        self.target_x = None
        self.target_y = None
        self.target_reached = False

        #current orientation
        self.current_orientation = None

        #depth first search
        # self.queue = [((x, y), direction)] - structure
        self.queue = []
        #shortest_path
        self.shortest_path = []

    def start(self, client, logger):

        planet = Planet()
        com = Communication(client, logger, self, planet)
        color = Color()
        color.color_calibration()

        com.client.loop_start()
        # com.send_testplanet("Boseman")

        #Movement
        m = Movement(self, com, color, planet)
        m.go_to_first_node()
        m.explore()
        
        #checking if all nodes were visited
        looping = True
        while looping:
            # checking for shortest path
            self.shortest_path = []
            #creating unvisited - list
            nearest_nodes = []
            for node in list(planet.get_paths()):
                if node not in m.visited:
                    if len(planet.get_paths()[node].values()) == 4:
                        m.visited.append(node)
                    else:
                        nearest_nodes.append(node)

            # find nearest node
            sp_weight_list = []
            for node in nearest_nodes:
                tmp_sp = planet.shortest_path((self.end_x,self.end_y), node)
                # calc path weight
                path_weight = 0
                if tmp_sp:
                    for (node, direction) in tmp_sp:
                        for dir, (_, _, weight) in planet.get_paths()[node].items():
                            if dir == direction:
                                path_weight += weight
                    sp_weight_list.append((tmp_sp, path_weight))

            if sp_weight_list:
                self.shortest_path = min(sp_weight_list, key = lambda t: t[1])[0]
                
            if self.shortest_path:
                i = 0
                while i < len(self.shortest_path):
                    m.go_to(self.shortest_path[i])  
                    i += 1

            m.explore()

            #checking if a target is selected
            if self.target_x is not None and self.target_y is not None:
                m.go_to_target()
                if self.target_reached:
                    looping = False 

            
            #checking if a new node is not visited or reachable nodes
            missing_reachable_node = False
            for node in planet.get_paths():
                if node not in m.visited:
                    tmp_sp = planet.shortest_path((self.end_x,self.end_y), node)
                    if tmp_sp:
                        missing_reachable_node = True
                        break
            if missing_reachable_node:
                continue
                       
            # end while-loop
            looping = False              

        if not self.target_reached:
            com.send_exploration_completed()

        com.client.loop_stop()
        com.client.disconnect()

