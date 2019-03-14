from ClaudClient import ClaudClient
import pickle
import os


def main():

    try:
        sessionCookies = None
        if os.path.getsize('files/cookiejar') > 0:         
            with open('files/cookiejar', 'rb') as f:
                sessionCookies = pickle.load(f)

        claud = ClaudClient(sessionCookies)
        sessionCookies = claud.getSession()
        claud.listen()

        with open('files/cookiejar', 'wb') as f:
            pickle.dump(sessionCookies, f)

    except Exception:
        return


if __name__ == '__main__':
    main()