#!/usr/bin/python3
"""Return Pascal's triangle"""


def pascal_triangle(n):
    """Function  to return Pascals's triangle"""
    rows = []
    if (n > 0):
        rows.append([1])
        for row_num in range(1, n):
            new_row = []
            prev_row = rows[row_num-1]
            m = len(prev_row)
            for i in range(m+1):
                if i==0:
                    new_row.append(prev_row[i])
                elif i==m:
                    new_row.append(prev_row[i-1])
                else:
                    new_row.append(prev_row[i-1]+prev_row[i])

            rows.append(new_row)

            """ row = rows[row_num - 1]
            new_row = []
            m = len(row)
            for i in range(m + 1):
                x = i - 1
                if x < 0 or i == m:
                    if i == m:
                        idx = i - 1
                    else:
                        idx = i
                    new_row.append(row[idx] + 0)
                else:
                    new_row.append(row[x] + row[i])
            rows.append(new_row) """
    return rows 
