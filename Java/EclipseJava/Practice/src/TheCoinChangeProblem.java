public class TheCoinChangeProblem
{
    public static long countWaysOfPayingWithCoins(int totalMoney, long[] coins)
    {
        return countWaysOfPayingWithCoinsRecursive(totalMoney, coins, 0, new HashMap<String, Long>());
    }

    private static long countWaysOfPayingWithCoinsRecursive(int totalMoney, long[] coins, int coinIndex, Map<String, Long> amountToWaysCountMap)
    {
        if (totalMoney == 0)
        {
            return 1;
        }

        if (coinIndex >= coins.length)
        {
            return 0;
        }

        String key = totalMoney + "-" + coinIndex;
        if (amountToWaysCountMap.containsKey(key))
        {
            return amountToWaysCountMap.get(key);
        }

        long waysToPay = 0;

        int maxAmountToPayWithCoinType = 0;
        while (maxAmountToPayWithCoinType <= totalMoney)
        {
            int remainingMoney = totalMoney - maxAmountToPayWithCoinType;
            waysToPay += countWaysOfPayingWithCoinsRecursive(remainingMoney, coins, coinIndex + 1, amountToWaysCountMap);
            maxAmountToPayWithCoinType += coins[coinIndex];
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
