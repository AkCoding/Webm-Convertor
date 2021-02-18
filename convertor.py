import subprocess

class FFMConvertor:
    try:
        def convert_webm_to_mp4_using_subprocess(self, input_file, output_file):
            command = 'ffmpeg -i ' + input_file +' -crf 23 '+ output_file
            print(command)
            subprocess.run(command)
    except:
        print("some exception")


ffm = FFMConvertor()
ffm.convert_webm_to_mp4_using_subprocess('/home/hb/Downloads/small.webm', '/home/hb/Downloads/smallaa.mp4')