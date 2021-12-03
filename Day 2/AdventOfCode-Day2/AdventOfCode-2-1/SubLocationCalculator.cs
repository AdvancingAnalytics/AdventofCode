using System;

namespace AdventOfCode_2_1
{
    public class SubLocationCalculator
    {
        public SubLocation GetSubLocation(string[] commands)
        {
            var location = new SubLocation();

            foreach (var command in commands)
            {
                if (command.Contains("forward")) {
                    var input = int.Parse(command.Replace("forward ", ""));
                    location.Horizontal = location.Horizontal + input;
                }

                if (command.Contains("down")) {
                    var input = int.Parse(command.Replace("down ", ""));
                    location.Depth = location.Depth + input;
                }

                if (command.Contains("up")) {
                    var input = int.Parse(command.Replace("up ", ""));
                    location.Depth = location.Depth - input;
                }
            }

            return location;
        }

        public SubLocationWithAim GetSubLocationWithAim(string[] commands)
        {
            var location = new SubLocationWithAim();

            foreach (var command in commands)
            {
                if (command.Contains("forward")) {
                    var input = int.Parse(command.Replace("forward ", ""));
                    location.Horizontal = location.Horizontal + input;

                    location.Depth = location.Depth + (input * location.Aim);
                }

                 if (command.Contains("down")) {
                    var input = int.Parse(command.Replace("down ", ""));
                    location.Aim = location.Aim + input;
                }

                if (command.Contains("up")) {
                    var input = int.Parse(command.Replace("up ", ""));
                    location.Aim = location.Aim - input;
                }
            }

            return location;
        }
    }
}