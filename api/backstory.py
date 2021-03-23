class Backstory:

    def __init__(self):
        self.lifegoal = self.__gen_life_goal()
        self.fears = self.__gen_fears()
        self.pride = self.__gen_pride()

    def gen_life_goal(self):
        return ''

    def __gen_fears(self):
        return ''

    def __gen_pride(self):
        return ''

    def __str__(self):
        return "Life Goal: {}\nGreatest Fears: {}\nFeels Pride About: {}".format(self.lifegoal, self.fears, self.pride)


def get(request):
    backstory = Backstory()
    
    return backstory.__str__()
