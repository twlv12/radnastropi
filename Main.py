if __name__ == "__main__":

    #Call all modules here


    import CoreMethods as core
    from time import sleep


    for i in range(5):
        sleep(1)
        gps = core.getNowGPS()
        print(f"got GPS now {gps}")
        img = core.getImage(f'0{i}', GPS=gps)
        print(f"got image {img}")

    input()