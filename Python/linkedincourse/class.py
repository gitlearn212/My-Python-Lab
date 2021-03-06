class Duck():
    def quack(self):
        print("Quaak")

    def walk(self):
        print("walks like a duck")


def main():

    donald = Duck()         # donald is an object of the class Duck means donald = duck()
    donald.quack()          # call the object (class Duck assigned to donald) donald and the method quaak and walk (def quaak and def walk())
    donald.walk()

    # Duck.quaak() # does not work so Duck must be assinged to an object such as above
    # Duck.walk()


if __name__ == '__main__':
    main()
