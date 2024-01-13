# 九九乘法表

import random

class Student:
    def __init__(self, position):
        self.position = position

    def move(self, target_position, speed):
        # 模拟学生移动过程
        distance = abs(target_position - self.position)
        time_required = distance / speed
        return time_required

def evacuation_simulation(num_students, hall_radius, door_width, average_speed):
    # 初始化学生的位置
    students = [Student(random.uniform(0, hall_radius)) for _ in range(num_students)]

    # 模拟疏散过程
    total_evacuation_time = 0
    for student in students:
        door_position = hall_radius  # 门的位置设在圆形大礼堂的右侧
        evacuation_time = student.move(door_position, average_speed)
        total_evacuation_time += evacuation_time

    # 计算平均疏散时间
    average_evacuation_time = total_evacuation_time / num_students
    return average_evacuation_time

# 模拟参数
num_students = 300
hall_radius = 20  # 大礼堂半径
door_width = 2
average_speed = 1.0  # 学生平均移动速度

# 运行模拟
result = evacuation_simulation(num_students, hall_radius, door_width, average_speed)
print(f"平均疏散时间: {result} 秒")
