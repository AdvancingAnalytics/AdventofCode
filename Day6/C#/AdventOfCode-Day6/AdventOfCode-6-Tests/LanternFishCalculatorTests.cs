using Microsoft.VisualStudio.TestTools.UnitTesting;
using AdventOfCode_6;
using System.IO;
using System.Linq;

namespace AdventOfCode_6_Tests
{
    [TestClass]
    public class SubBinaryDiagnosticTests
    {
        [TestMethod]
        public void GenerateFish_WhenCreatingOneFish_ReturnSingleFish()
        {
            // arrange
            var fishCalc = new LanternFishCalculator();

            // act
            var newFishes = fishCalc.GenerateFish("1");

            // assert
            Assert.AreEqual(1, newFishes.Count());
        }

        [TestMethod]
        public void SpawnFish_WhenOneFishAgedOne_ReturnTwoFishes()
        {
            // arrange
            var fishCalc = new LanternFishCalculator();
            var newFishes = fishCalc.GenerateFish("1");

            // act
            var allFishes = fishCalc.SpawnFish(newFishes, 1);

            // assert
            Assert.AreEqual(2, allFishes.Count());
        }

        [TestMethod]
        public void SpawnFish_WhenUsingSampleInput1Day_ReturnSampleResults()
        {
            // arrange
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var fishCalc = new LanternFishCalculator();
            var newFishes = fishCalc.GenerateFish(lines[0]);

            // act
            var allFishes = fishCalc.SpawnFish(newFishes, 1);

            // assert
            Assert.AreEqual(5, allFishes.Count());
        }

        [TestMethod]
        public void SpawnFish_WhenUsingSampleInput_ReturnSampleResults()
        {
            // arrange
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var fishCalc = new LanternFishCalculator();
            var newFishes = fishCalc.GenerateFish(lines[0]);

            // act
            var allFishes = fishCalc.SpawnFish(newFishes, 18);

            // assert
            Assert.AreEqual(26, allFishes.Count());
        }

        [TestMethod]
        public void SpawnFish_WhenUsingSampleInput80Days_ReturnSampleResults()
        {
            // arrange
            var lines = File.ReadAllLines("../../../SampleData.txt");

            var fishCalc = new LanternFishCalculator();
            var newFishes = fishCalc.GenerateFish(lines[0]);

            // act
            var allFishes = fishCalc.SpawnFish(newFishes, 80);

            // assert
            Assert.AreEqual(5934, allFishes.Count());
        }
    }
}