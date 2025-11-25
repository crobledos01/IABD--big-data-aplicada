from mrjob.job import MRJob
from statistics import mean
import sys

class MarksMR(MRJob):
    
    def mapper(self, _, line):
        if isinstance(line, bytes):
            line = line.decode('utf-8', errors='replace')
        line = line.strip()
        if not line:
            return
        if ',' in line:
            parts = [p.strip() for p in line.split(',') if p.strip()]
        else:
            parts = line.split()
        if len(parts) < 2:
            return
        name, *marks = parts
        for mark in marks:
            yield name, float(mark)

    def reducer(self, name, marks):
        marks_list = list(marks)
        if marks_list:
            yield name, mean(marks_list)

if __name__ == '__main__':
    MarksMR.run()