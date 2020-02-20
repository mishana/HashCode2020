from optimization.optimizer import OutData, InData


def calc_score(solution: OutData, in_data: InData) -> float:
    T = 0
    scanned_books = set()

    for l in solution.Libraries:
        T += in_data.Libraries[l.Y].T
        days_of_scan = in_data.D - T

        books_to_scan = set(l.Books[:(days_of_scan * in_data.Libraries[l.Y].M)])
        scanned_books = scanned_books | books_to_scan

    score = 0
    for b in scanned_books:
        score += in_data.Scores[b]

    return score


# MORE FUNCTIONS THAT ARE COMMON FOR DIFFERENT OPTIMIZERS ARE GOING TO BE PLACED HERE