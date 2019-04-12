public class TheCoinChangeProblem
{
    static long countWaysOfPayingWithCoins(int totalMoney, long[] coins)
    {
        return countWaysOfPayingWithCoinsRecursive(totalMoney, coins, 0, new HashMap<String, Long>());
    }

    static long countWaysOfPayingWithCoinsRecursive(int totalMoney, long[] coins, int index, HashMap<String, Long> amountToWaysCountMap)
    {
        if (totalMoney == 0)
        {
            return 1;
        }

        if (index >= coins.length)
        {
            return 0;
        }

        String key = totalMoney + "-" + index;
        if (amountToWaysCountMap.containsKey(key))
        {
            return amountToWaysCountMap.get(key);
        }

        long waysToPay = 0;

        int maxAmountToPayWithCoinType = 0;
        while (maxAmountToPayWithCoinType <= totalMoney)
        {
            int remainingMoney = totalMoney - maxAmountToPayWithCoinType;
            waysToPay += countWaysOfPayingWithCoinsRecursive(remainingMoney, coins, index + 1, amountToWaysCountMap);
            maxAmountToPayWithCoinType += coins[index];
            amountToWaysCountMap.put(key, waysToPay);
        }

        return waysToPay;
    }

    public static void main(String[] args)
    {
        int totalMoneyToPay = 15;
        long[] coins = {49, 22, 45, 6, 11, 20, 30, 10, 46, 8, 32, 48, 2, 41, 43, 5, 39, 16, 28, 44, 14, 4, 27, 36};
        long ways = countWaysOfPayingWithCoins(totalMoneyToPay, coins);
        System.out.println(ways);
    }
}
