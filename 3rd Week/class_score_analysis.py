def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            row = list(map(int, line.strip().split(',')))
            data.append(row)
    return data

def calc_weighted_average(data_2d, weight):
    average = []
    for row in data_2d:
        weighted_avg = row[0] * weight[0] + row[1] * weight[1]
        average.append(weighted_avg)
    return average

def analyze_data(data_1d):
    mean = sum(data_1d) / len(data_1d)
    sum_squared = 0
    for datum in data_1d:
        sum_squared += datum**2
    var = sum_squared / len(data_1d) - mean**2
    sorted_data_1d = sorted(data_1d)
    n = len(sorted_data_1d)
    if n % 2 == 1:
        median = sorted_data_1d[n // 2]
    else:
        median = (sorted_data_1d[n // 2 - 1] + sorted_data_1d[n // 2]) / 2
    return mean, var, median, min(data_1d), max(data_1d) 

if __name__ == '__main__':
    data = read_data('C:/Users/data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Average |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
                