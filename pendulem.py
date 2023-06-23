import numpy as np
import matplotlib.pyplot as plt

# 입력 받기          
theta = float(input('초기 각 입력 : '))  # 초기각도
theta_rad = np.deg2rad(theta)  # 라디안으로 변환
l = 5  # 단진자 길이
g = 9.81
t = np.linspace(0, 10, 200)  # 0부터 10초까지 200개 구간으로 나누기
s_f = 0
interval = 30

# 초기 위치와 속도 계산
x = l * np.sin(theta_rad)
y = -l * np.cos(theta_rad)

# 그래프 설정
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(6, 8))
ax1.set_aspect("equal")  # 정사각형으로 만들기
ax1.axes.xaxis.set_visible(False)  # x 좌표값 없애기
ax1.axes.yaxis.set_visible(False)  # y 좌표값 없애기
ax1.set_xlim(-6, 6)  # x축 범위 설정
ax1.set_ylim(-6, 1)  # y축 범위 설정
line, = ax1.plot([], [], color='mediumspringgreen')  # 선 색상
circle = plt.Circle((x, y), 0.5, color='aqua')  # 진자 색상
ax1.add_artist(circle)  # circle 객체 추가

# 에너지 그래프 설정
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 50)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Energy (J)')
ax2.axhline(y=0, color='gray', linestyle='--')
kinetic_line, = ax2.plot([], [], label='Kinetic Energy', color='palegreen')
potential_line, = ax2.plot([], [], label='Potential Energy', color='cornflowerblue')
total_line, = ax2.plot([], [], label='Total Energy', color='violet')
ax2.legend()


# 에너지 계산 함수
def calc_energy(theta_rad, s_f):
    E_kinetic = 0.5 * l ** 2 * s_f ** 2
    E_potential = l * g * (1 - np.cos(theta_rad))
    E_total = E_kinetic + E_potential
    return E_kinetic, E_potential, E_total


kinetic_energies = []
potential_energies = []
total_energies = []

for i in range(len(t)):
    E_kinetic, E_potential, E_total = calc_energy(theta_rad, s_f)
    kinetic_energies.append(E_kinetic)
    potential_energies.append(E_potential)
    total_energies.append(E_total)
    s_f += (-g / l) * np.sin(theta_rad) * (t[1] - t[0])
    theta_rad += s_f * (t[1] - t[0])
    x = l * np.sin(theta_rad)
    y = -l * np.cos(theta_rad)
    circle.center = (x, y)
    line.set_data([0, x], [0, y])
    kinetic_line.set_data(t[:i + 1], kinetic_energies)
    potential_line.set_data(t[:i + 1], potential_energies)
    total_line.set_data(t[:i + 1], total_energies)
    plt.pause(interval / 1000)

plt.show()
