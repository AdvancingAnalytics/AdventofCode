using System;
using System.Collections.Generic;

namespace AdventOfCode_6
{
    public class LanternFishCalculator
    {
        public IEnumerable<LanternFish> GenerateFish(string fishInput)
        {
            // split the input on ,
            var daysToSpawn = fishInput.Split(',');

            List<LanternFish> initialFish = new List<LanternFish>();

            // generate a fish for each of the inputs
            foreach (var days in daysToSpawn)
            {
                var numOfDays = int.Parse(days);

                // add fish to collection
                initialFish.Add(new LanternFish(numOfDays));
            }

            // return initial fish collection
            return initialFish;
        }

        public IEnumerable<LanternFish> SpawnFish(IEnumerable<LanternFish> initialFish, int numOfDays)
        {
            if (numOfDays == 0)
                return initialFish;

            List<LanternFish> allFish = new List<LanternFish>();            

            foreach (var fish in initialFish)
            {
                var newFish = fish.AgeOneDay();

                if (newFish != null)
                    allFish.Add(newFish);

                allFish.Add(fish);
            }

            var newNumOfDays = numOfDays - 1;
            return SpawnFish(allFish, newNumOfDays);
        }
    }
}