#Data
hour = 6
minute = 52
easy_pace_distance = 1 + 2  #miles
tempo_distance = 3  #miles

#Evaluation of running duration
easy_pace_duration = easy_pace_distance * 8 #minutes
tempo_duration = tempo_distance * 6  #minutes
total_duration = easy_pace_duration + tempo_duration

#Formatting the output
output_minute = (minute + total_duration) % 60
output_hour = hour + (minute + total_duration) // 60

#output
print(output_hour, ":", output_minute)