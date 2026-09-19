import os
import sys

sumo_home = os.environ.get('SUMO_HOME')

if not sumo_home:
    print("❌ خطأ: متغير البيئة SUMO_HOME غير معرّف على هذا الجهاز.")
    print("💡 يرجى تعريفه في متغيرات النظام ليعمل الكود.")
    sys.exit(1)

sys.path.append(os.path.join(sumo_home, 'tools'))

import traci

current_dir = os.path.dirname(os.path.abspath(__file__))

sumoBinary = os.path.join(sumo_home, 'bin', 'sumo-gui.exe')

sumoConfig = ["-c", os.path.join(current_dir, 'ASTLS.sumocfg')]

TL_ID = "clusterJ4_J5"

try:
    traci.start([sumoBinary] + sumoConfig)
    print("✅ تم الاتصال بنجاح وبدأت محاكاة الإشارات المرورية الذكية!")
    
    step = 0
    while step < 3000:
        traci.simulationStep()
        
        if step % 50 == 0:
            controlled_lanes = traci.trafficlight.getControlledLanes(TL_ID)
            
            max_queue = -1
            selected_phase = 0
            
            for i, lane in enumerate(controlled_lanes):
                waiting_cars = traci.lane.getLastStepHaltingNumber(lane)
                
                if waiting_cars > max_queue:
                    max_queue = waiting_cars
                    selected_phase = (i % 4) * 2  
            
            if max_queue > 2:
                traci.trafficlight.setPhase(TL_ID, selected_phase)
                print(f"🚦 الخطوة {step}: تم تغيير الإشارة للطور الأخضر {selected_phase} بسبب وجود {max_queue} سيارات منتظرة.")
                
        step += 1
        
    traci.close()
    print("🏁 انتهت المحاكاة الذكية بنجاح.")
    
except Exception as e:
    print("❌ حدث خطأ أثناء التشغيل:", e)