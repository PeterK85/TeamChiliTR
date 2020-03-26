import chili

# NO TOUCHY
file_name = chili.init_tr("10", "3.27.20")
# END NO TOUCHY

# To add a meeting, put a string in the list ex. "Client meeting"
meetings = ["Client Zoom Meeting 3.27.20"]
chili.recent_meetings(file_name, meetings)

# Adding a new task
# chili.new_task(file_name,
#                task title,
#                initiation date,
#                due date,
#                status,
#                who, WARNING - put \\ before % sign
#                description,
#                outcome)
chili.new_section(file_name, "TASKS COMPLETED since last meeing")
chili.new_task(file_name,
               "Create a script to make these task reports easier to make",
               "3.25.20",
               "3.26.20",
               "100",
               "Peter (95\\%) Adam (5\\%)",
               "Write a python script that auto generates a pdf of the task report so we don't have to mess around with google docs' terrible copy and paste.",
               "Code written and tested and working.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "Researched and wrote code for remotely powering on the RPi",
               "3.6.20",
               "3.12.20",
               "100",
               "Michael (100\\%)",
               "Explored options for remotely powering on and off Pi.",
               "Powering off can be done through the command line. RPi does not support WOL (Wake on Lan) through its ethernet ports so we needed to interface with the Ethernet Power Controller on site. Code complete and demonstrated in demo.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_section(file_name, "This week’s Tasks: Work plan for coming week")
chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_section(file_name, "Upcoming Tasks: Planning")
chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

chili.new_task(file_name,
               "PiGPIO lib in C",
               "3.6.20",
               "3.13.20",
               "100",
               "Michael (50\\%) Adam (50\\%)",
               "After getting Jim's approval that the library is outputting the correct signal, start implementing code to use PiGPIO in C.",
               "Code written and tested.")

# NO TOUCHY
chili.finish_the_chili(file_name)
# END NO TOUCHY