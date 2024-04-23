# Return True if class photos can be taken with students with the following heights
# Rule1: same colored shirt-wearing students should be in the same row
# Rule2: all students in the last row should be strictly taller than the student in the front row


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    # Write your code here.
    diff1 = [x > y for x, y in zip(redShirtHeights, blueShirtHeights)]
    diff2 = [x < y for x, y in zip(redShirtHeights, blueShirtHeights)]

    return all(diff1) or all(diff2)
