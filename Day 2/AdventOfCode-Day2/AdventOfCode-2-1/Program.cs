using System;
using System.IO;

namespace AdventOfCode_2_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculating Submarine Location");

            var lines = File.ReadAllLines("puzzleinput2.txt");
            var subLocationCalculator = new SubLocationCalculator();

            var puzzle1Result = subLocationCalculator.GetSubLocation(lines);            
            var puzzle1Value = puzzle1Result.Depth * puzzle1Result.Horizontal;
            Console.WriteLine($"Puzzle 1 calculated value is: {puzzle1Value}");

            var puzzle2Result = subLocationCalculator.GetSubLocationWithAim(lines);            
            var puzzle2Value = puzzle2Result.Depth * puzzle2Result.Horizontal;
            Console.WriteLine($"Puzzle 2 calculated value is: {puzzle2Value}");
        }
    }
}
