import ffmpeg


class FFm:
    def convertor(self, input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(stream)

        except:
            print('some Exception')

fm = FFm()
fm.convertor(r'/home/hb/Downloads/small.webm', r'/home/hb/Downloads/small.mp4')