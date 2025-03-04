## ASIAIR Jailbreak
All code was written by joshumax this simply stored on GitHub as this is being released under public domain. All files and text were taken from https://www.cloudynights.com/topic/900861-seestar-s50asiair-jailbreak-ssh/

### FIRST OF ALL, THIS IS ALL ESSENTIALLY ONE GIANT HACK. IT HAS WORKED FOR ME BUT IT COULD BRICK YOUR DEVICE, OR WORSE. THIS IS FOR DEVELOPERS ONLY. IF YOU AREN'T FAMILIAR WITH SSH OR LINUX, DON'T USE THIS!

Hi everyone,

With the release of ZWO's new Seestar S50, I'm finally releasing a tool I've been using internally to gain root SSH access to both my Seestar and ASIAIR devices. I was originally hoping that ZWO would reduce their rampant open source software license violations and vendor lock-in, but it's only gotten worse. This has made me decide to create a completely FOSS integrated astrophotography solution that will totally replace their software while still leveraging the ASI hardware. I intend to release this project free of charge to the astronomical community shortly.

In the meantime, I am providing this jailbreak so that others can explore their ASIAIR device without the need of physically opening it and soldering on UART headers. To run it, all you need is a machine running a reasonably new Python 3 as well as the archive attached to this post.

Current jailbreak release
https://mega.nz/file/1cRQjbCL#zs6TYY8k8ycevjFhr9xV7GDWmo70hMvRt3E0ym0GGXY


### Run jailbreak:
```	
python run_jailbreak.py [IP_ADDRESS_OF_DEVICE]
```
### Connect to Seestar/ASIAIR:
```	
ssh pi@[IP_ADDRESS_OF_DEVICE]
```	
### The password for SSH will be "raspberry" (no quotes) if the jailbreak ran successfully. You can access the root account via "sudo".