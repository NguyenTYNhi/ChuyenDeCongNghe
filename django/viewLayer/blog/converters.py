class FourDigitYearConverter:
    regex = "[0-9]{4}"  # chỉ cho phép 4 chữ số

    def to_python(self, value):
        # chuyển giá trị string -> int
        return int(value)

    def to_url(self, value):
        # chuyển int -> string khi reverse url
        return "%04d" % value
