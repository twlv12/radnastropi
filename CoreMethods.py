#Contains all base methods for the astro pi

print("CoreMethods loading")
import astro_pi_orbit as orbit
import picamzero as piCam
print("CoreMethods loaded")


def getImage(imageId, GPS=None):
    print("Getting Image")
    camera = piCam.Camera()
    camera.take_photo(f'image_{imageId}.jpg')
    return f'image_{imageId}.jpg'


def getNowGPS():
    print("Getting GPS Now")
    iss = orbit.ISS()
    gps = iss.coordinates()
    signedGPS = (gps.latitude.signed_dms(), gps.longitude.signed_dms())
    return signedGPS


#use for atTime::: 
#from skyfield.api import load
#ts=load.timeScale()
#ts.utc(year,month,day,hour,minute)
def getTimeGPS(atTime):
    print(f"Getting GPS {atTime}")
    iss = orbit.ISS()
    gps = iss.at(atTime)
    signedGPS = (gps.latitude.signed_dms(), gps.longitude.signed_dms())
    return signedGPS


def getEarthData():
    print("Getting Earth Object")
    from astro_pi_orbit import de421
    earth = de421["earth"]
    return earth
    