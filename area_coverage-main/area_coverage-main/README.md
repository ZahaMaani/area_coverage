# Robots and Autonomous Systems Course Project
The goal of this project is to implement and evaluate a complete coverage path planning algorithm for a mobile robot operating within a bounded rectangular area. The robot must autonomously navigate from any starting position within the area to a defined origin point, and then systematically cover the entire area while detecting and avoiding obstacles in real time.

The primary research question is: ***How can a mobile robot efficiently achieve full coverage of a bounded rectangular area using a systematic path planning strategy, while dynamically responding to obstacles detected by onboard sensors?***

---
## Coverage Algorithm
We plan to investigate and implement the following coverage strategies, selecting the most appropriate based on preliminary experiments:
- Boustrophedon decomposition (lawn-mower pattern): the robot traverses parallel rows across the area, reversing direction at each boundary. This approach is simple and well-studied for rectangular environments.
- Spiral coverage: the robot moves in progressively inward (or outward) concentric loops. This may be evaluated as an alternative or baseline for comparison.

## Obstacle Avoidance
Obstacles are not known in advance. The robot will rely on sensors to detect obstacles in real time. Upon detection, the robot will apply a local avoidance maneuver (e.g. stop, rotate, detour) and then re-integrate into the planned coverage path to minimize missed areas.

---
***This project will be carried out by Salahaldeen Alquraan and Zaha Maani***
