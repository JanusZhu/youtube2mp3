def main():
    from pytube import YouTube
    import os
    from pathlib import Path
    def youtube2mp3 (url,outdir):
        # url input from user
        yt = YouTube(url)

        ##@ Extract audio with 160kbps quality from video
        video = yt.streams.filter(abr='160kbps').last()

        ##@ Downloadthe file
        out_file = video.download(output_path=outdir)
        base, ext = os.path.splitext(out_file)
        new_file = Path(f'{base}.mp3')
        os.rename(out_file, new_file)
        ##@ Check success of download
        if new_file.exists():
            print(f'{yt.title} has been successfully downloaded.')
        else:
            print(f'ERROR: {yt.title}could not be downloaded!')
    url =str(input("Enter the URL of the video you want to download: \n>> "))
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
    youtube2mp3(url, destination)
  
main();