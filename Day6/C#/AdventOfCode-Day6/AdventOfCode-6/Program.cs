using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode_6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculating Lantern Fish counts");

            var lines = File.ReadAllLines("puzzleinput.txt");
            var lanternFishCalc = new LanternFishCalculator();

            var initialFish = lanternFishCalc.GenerateFish(lines[0]);
            var puzzle1Result = lanternFishCalc.SpawnFish(initialFish, 80);

            var count = puzzle1Result.Count().ToString();
            Console.WriteLine($"Puzzle 1 calculated value is: {count}");

            // var puzzle2Value = puzzle1Result.CO2ScrubberRate * puzzle1Result.OxygenRate;
            // Console.WriteLine($"Puzzle 2 calculated value is: {puzzle2Value}");
        }
    }
}
