
        def boyer_moore(arr):
            cnt = 0
            maj = float("inf")
            for v in arr:
                if cnt == 0:
                    maj = v
                if v == maj:
                    cnt += 1
                else:
                    cnt -= 1
            return maj