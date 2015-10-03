import lumiversepython as L

rig = L.Rig("../home/teacher/Lumiverse/Pbridge.rig.json");
rig.init();
rig.run();
rig.select("$panel=31").setRGBRaw(1,0,0);