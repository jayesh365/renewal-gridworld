from __future__ import annotations
from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Wall, Floor
from minigrid.manual_control import ManualControl
from minigrid.minigrid_env import MiniGridEnv

class SimpleEnv(MiniGridEnv):
    def __init__(
        self,
        size=12,
        agent_start_pos=(10, 1),
        agent_start_dir=2,
        max_steps: int | None = None,
        highlight_mask: bool = False,
        **kwargs,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        mission_space = MissionSpace(mission_func=self._gen_mission)

        super().__init__(
            mission_space=mission_space,
            grid_size=size,
            max_steps=256,
            **kwargs,
        )

    @staticmethod
    def _gen_mission():
        return "ROBOTS DAY"
    
    def _gen_grid(self, width, height):
        # create an empty grid
        self.grid = Grid(width, height)
        
        # create a wall around the grid
        self.grid.wall_rect(0, 0, width, height)
        
        # place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()
        
        # create workstation and chargestation        
        self.put_obj(Floor(color='green'), 10, 1)
        self.put_obj(Floor(color='yellow'), 1, 10)
        
        
        
        
        
        # create walls
        for i in range(0, 4):
            self.grid.set(5, i, Wall())
        
        for i in range(8, 11):
            self.grid.set(5, i, Wall())
        

        for i in range(0, 5):
            self.grid.set(4, i, Wall())

        for i in range(0, 6):
            self.grid.set(3, i, Wall())
            self.grid.set(2, i, Wall())
            self.grid.set(1, i, Wall())
            
        for i in range(7, 11):
            self.grid.set(6, i, Wall())
        
        
        for i in range(6, 11):
            self.grid.set(7, i, Wall())
            self.grid.set(8, i, Wall())
            self.grid.set(9, i, Wall())
            self.grid.set(10, i, Wall())
            

def main():
    env = SimpleEnv(render_mode="human")

    # enable manual control for testing
    manual_control = ManualControl(env, seed=42)
    manual_control.start()

    
if __name__ == "__main__":
    main()