from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(And(self._matcher, Or(matcher1, matcher2)))
