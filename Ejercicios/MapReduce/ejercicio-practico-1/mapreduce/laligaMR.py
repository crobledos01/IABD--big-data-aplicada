from mrjob.job import MRJob
from mrjob.step import MRStep

class LaLigaMR(MRJob):
    def mapper_points(self, _, line):
        _, _, _, home_team, away_team, _, _, result, *rest = line.split(',')
        if home_team == "HomeTeam":
            return
        
        if result == 'D':
            yield home_team, 1
            yield away_team, 1
        elif result == 'H':
            yield home_team, 3
        else:
            yield away_team, 3

    def combiner_points(self, team, points):
        yield team, sum(points)
        
    def reducer_points(self, team, points):
        yield None, (team, sum(points))

    def reducer_classification(self, _, points):
        yield None, sorted(points, key=lambda t: t[1], reverse=True)
        
    def steps(self):
        return [
            MRStep(mapper=self.mapper_points,
                   combiner=self.combiner_points,
                   reducer=self.reducer_points,
                   MRStep(reducer=self.reducer_classification))
        ]