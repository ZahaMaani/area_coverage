## Developer Journal - [Coverage Project]

### [2026-07-02] - Team Session
At the start of the project, we wanted to compare between the L-Shaped Boustrophedon Method and the Spiral method to cover an enclosed area. To do so, we needed the robot to start the coverage at any of the corners of the area, while also being parallel to the border line -which was the first thing we did in this session. After that we started brainstorming the ways in which we can implement the L-Shaped method, and came up with a preliminary solution that starts coverage of the area and enters an endless loop (without stopping). Therefore, we needed to find a way to stop the robot when it detects that the entire area was covered. 

**Next Step:**
* Implement a termination condition to detect complete room coverage and halt execution.
* Implement a way for the robot to cover the area using the spiral method.
* Compare the two methods to find which is more suitable for the proposed problem. 

---

### [2026-07-04] - Team Session
In this session, we found a solution for the endless loop that the robot goes through during the L-Shaped method. After that, we implemented the spiral method for the robot which was easier to implement as it was logically easier to code. 

After the completion of both methods initially (without any obstacles), we measured the time it took for our robot to cover the same area using both methods for two main reasons. First, this measurement is the clear answer to our problem statement. Second, the method that takes less time will go through further improvements including obstacle avoidance and real time tracking. Accordingly, the time it took for the robot to cover the area using: 
* Boustrophedon Method was **39 seconds**
* Spiral Method was **47 seconds** 

Accordingly, we started the implementation of the obstacle avoidance. This however had one main flaw, where it could go over the border is the obstacle was the same length of the side (a wall).  

**Next Step:**
* Enforce boundary constraints to ensure the robot remains within the designated area during obstacle avoidance maneuvers.

---

### [2026-07-11] - Team Session

* Advanced the implementation and refinement of the obstacle avoidance module.
* Integrated data visualization features using `matplotlib` to dynamically plot and track the covered area.
