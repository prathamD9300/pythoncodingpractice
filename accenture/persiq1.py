def bandMemberAt(totalMembers, SwapMembers, posMember):
    bandMembers = list(range(1, totalMembers + 1))

    for swaps in SwapMembers:
        for i in range(0, len(swaps), 2):
            bandMembers[swaps[i] - 1], bandMembers[swaps[i + 1] - 1] = bandMembers[swaps[i + 1] - 1], bandMembers[swaps[i] - 1]

    finalPosition = bandMembers[posMember - 1]
    return finalPosition

def main():
    totalMembers = int(input())

    SwapMembers = []
    SwapMembersRows, SwapMembersCols = map(int, input().split())
    for idx in range(SwapMembersRows):
        SwapMembers.append(list(map(int, input().split())))

    posMember = int(input())
    result = bandMemberAt(totalMembers, SwapMembers, posMember)

    print(result)

if __name__ == "__main__":
    main()