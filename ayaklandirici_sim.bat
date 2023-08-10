@echo off

TITLE AYAKLANDIRICI

python -c "import psutil; import os; pid = psutil.Process(os.getppid()).pid; open('pid.txt', 'w').write(str(pid))"

python Ayaklandirici.py paths.xml

pause