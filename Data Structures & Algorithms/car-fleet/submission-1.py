class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        curr_time = fleet = 0
        for pos, speed in cars:
            dest_time = (target-pos) / speed
            print(pos,dest_time) 
            if dest_time > curr_time:
                fleet +=1 
                curr_time = dest_time
        return fleet