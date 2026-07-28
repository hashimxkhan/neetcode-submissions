class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        ret = 0
        for email in emails:
            flag = False
            new = ""
            for i in range(len(email)):
                if email[i] == '@':
                    flag = True
                    continue
                if email[i] == '.' and flag == False:
                    continue
                if email[i] == '+' and flag == False:
                    for j in range(i+1, len(email)):
                        if email[j] == '@':
                            new = new + email[j+1:]
                            break
                    break
                new+=email[i]
            if new not in seen:
                ret+=1
            seen.add(new)
        return ret