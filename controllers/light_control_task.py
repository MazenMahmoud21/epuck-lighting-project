from controller import Robot

def run_robot():
    # إنشاء نسخة الروبوت
    robot = Robot()
    
    # التأكد من الحصول على الـ timestep بشكل صحيح
    timestep = int(robot.getBasicTimeStep())
    if timestep == 0:
        timestep = 32 # قيمة احتياطية في حال وجود مشكلة في ملف العالم

    # 1. إعداد حساس الضوء
    ls = robot.getDevice('ls0')
    if ls:
        ls.enable(timestep)

    # 2. إعداد المصابيح
    leds = []
    for i in range(8):
        led = robot.getDevice(f'led{i}')
        if led:
            leds.append(led)

    print("--- Controller Started Successfully ---")

    # 3. الحلقة الرئيسية
    while robot.step(timestep) != -1:
        val = ls.getValue()

        if val > 2000.0:
            for led in leds:
                led.set(1)
            # print(f"Status: DARK ({val:.0f})") # عطل الـ print مؤقتاً لو الشاشة بتهنج
        else:
            for led in leds:
                led.set(0)
            # print(f"Status: LIGHT ({val:.0f})")

if __name__ == "__main__":
    run_robot()