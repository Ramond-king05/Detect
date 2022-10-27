import cx_Freeze

executables = [cx_Freeze.Executable("det.py")]

cx_Freeze.setup(
    name="Ramond Object Detector",
    options={"build_exe": {"packages":["seaborn","matplotlib","numpy","cv2","torch","pathlib","IPython","pygame"],
                           "include_files":["yolov5s.pt",r"C:\Users\user\Desktop\qaq\image\ff.jpg"]}},
    executables = executables

    )