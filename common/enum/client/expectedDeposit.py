import enum


class ExpectedDeposit(enum.Enum):
    deposit1 = '$50 - $999'
    deposit2 = '$1,000 - $9,999'
    deposit3 = '$10,000 - $49,999'
    deposit4 = '$50,000 - $249,999'
    deposit5 = '$250,000+'
