using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventOfCode_6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculating Lantern Fish counts");

            var lines = File.ReadAllLines("puzzleinput.txt");
            //var lanternFishCalc = new LanternFishCalculator();

            var count = CalculateFasterCount(lines[0], 80);

            // var initialFish = lanternFishCalc.GenerateFish(lines[0]);
            // var puzzle1Result = lanternFishCalc.SpawnFish(initialFish, 80);            

            // var count = puzzle1Result.Count().ToString();
            Console.WriteLine($"Puzzle 1 calculated value is: {count}");

            // var initialFish2 = lanternFishCalc.GenerateFish(lines[0]);
            // var puzzle2Result = lanternFishCalc.SpawnFish(initialFish2, 256);

            // count = puzzle2Result.Count().ToString();

            count = CalculateFasterCount(lines[0], 256);
            Console.WriteLine($"Puzzle 2 calculated value is: {count}");
        }

        public static int CalculateFasterCount(string fishInput, int numOfDays)
        {
            var fishAges = fishInput.Split(',');
            int totalCount = 0;
            int fishCount = 1;
            int[] cachedResult = new int[] {0, 0, 0, 0, 0, 0};

            foreach (var days in fishAges)
            {
                //List<LanternFish> initialFish = new List<LanternFish>();
                var daysToSpawn = int.Parse(days);
                // initialFish.Add(new LanternFish(daysToSpawn));

                // var fishWithChildren = SpawnFish(initialFish, numOfDays);

                int totalFishCount = 0;
                if (cachedResult[daysToSpawn] != 0)
                {
                    totalFishCount = cachedResult[daysToSpawn];
                }
                else
                {
                    totalFishCount = ReturnSingleFishChildCount(daysToSpawn, numOfDays);    
                    cachedResult[daysToSpawn] = totalFishCount;
                }                

                totalCount = totalCount + totalFishCount;

                Console.WriteLine($"Fish: {fishCount}, Total: {totalCount}");
                fishCount++;
            }

            return totalCount;
        }

        public static int ReturnSingleFishChildCount(int daysToSpawn, int numOfDays)
        {
            var lanternFishCalc = new LanternFishCalculator();

            List<LanternFish> initialFish = new List<LanternFish>();
            initialFish.Add(new LanternFish(daysToSpawn));
            var fishWithChildren = lanternFishCalc.SpawnFishRescursive(initialFish, numOfDays);

            return fishWithChildren.Count();
        }
    }
}
