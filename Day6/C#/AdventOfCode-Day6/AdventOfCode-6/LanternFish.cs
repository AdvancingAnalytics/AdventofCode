using System;

namespace AdventOfCode_6
{
    public class LanternFish
    {
        public int DaysToSpawn { get; set; }
        //public bool HasChild { get; set; }

        public LanternFish(int daysToSpawn)
        {
            DaysToSpawn = daysToSpawn;
        }

        public LanternFish AgeOneDay()
        {
            if (DaysToSpawn == 0)
            {
                // create a new fish
                //HasChild = true;
                DaysToSpawn = 6;
                return new LanternFish(8);                
            }

            DaysToSpawn--;

            return null;
        }
    }
}
