import math

class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty")

        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(x)
            else:
                raise TypeError(f"Invalid data type: {x}")

        self.data = cleaned
        self.n = len(cleaned)

    def get_mean(self):
        return sum(self.data) / self.n

    def get_median(self):
        sorted_data = sorted(self.data)
        mid = self.n // 2

        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        max_count = max(freq.values())

        if max_count == 1:
            return "All values are unique"

        return [k for k, v in freq.items() if v == max_count]

    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            return sum(squared_diffs) / (self.n - 1)
        return sum(squared_diffs) / self.n

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        return [x for x in self.data if abs(x - mean) / std > threshold]