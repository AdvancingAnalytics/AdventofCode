using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode_6
{
    public class LanternFishCalculator
    {
        public IEnumerable<LanternFish> GenerateFish(string fishInput)
        {
            // split the input on ,
            var fishAges = fishInput.Split(',');

            List<LanternFish> initialFish = new List<LanternFish>();

            // generate a fish for each of the inputs
            foreach (var days in fishAges)
            {
                var numOfDays = int.Parse(days);

                // add fish to collection
                initialFish.Add(new LanternFish(numOfDays));
            }

            // return initial fish collection
            return initialFish;
        }

        public IEnumerable<LanternFish> SpawnFishRescursive(IEnumerable<LanternFish> initialFish, int numOfDays)
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
            return SpawnFishRescursive(allFish, newNumOfDays);
        }

        public IEnumerable<LanternFish> SpawnFish(IEnumerable<LanternFish> initialFish, int numOfDays)
        {
            //if (numOfDays == 0)
                //return initialFish;
            List<LanternFish> allFish = initialFish.ToList();

            for (int i = 0; i < numOfDays; i++)
            {                
                var newFish = GetAllFish(allFish);    
                allFish = newFish;
            }

            return allFish;
        }

        public List<LanternFish> GetAllFish(IEnumerable<LanternFish> initialFish)
        {
            List<LanternFish> allFish = new List<LanternFish>();            

            foreach (var fish in initialFish)
            {
                var newFish = fish.AgeOneDay();

                if (newFish != null)
                    allFish.Add(newFish);

                allFish.Add(fish);
            }

            return allFish;
        }

        // public int CalculateFasterCount(string fishInput, int numOfDays)
        // {
        //     var fishAges = fishInput.Split(',');
        //     int totalCount = 0;

        //     foreach (var days in fishAges)
        //     {
        //         List<LanternFish> initialFish = new List<LanternFish>();
        //         var daysToSpawn = int.Parse(days);
        //         initialFish.Add(new LanternFish(daysToSpawn));

        //         var fishWithChildren = SpawnFish(initialFish, numOfDays);
        //         totalCount = totalCount + fishWithChildren.Count();                
        //     }

        //     return totalCount;
        // }
    }
}