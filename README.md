# Farm Path Detector

A Python simulation of path planning for an autonomous spraying robot moving between crop rows on a farm.

## Background

This project was inspired by watching a family member spray crops at night using a headlamp to find his way between rows. I wanted to explore how a simple program could plan a coverage path automatically instead of relying on manual navigation.

## Features

- The farm is represented as a grid: crop rows, open paths, and a start position
- Generates a full coverage path using a boustrophedon (back-and-forth) pattern — the same basic strategy real lawnmowers and agricultural machines use to cover a field without missing spots
- Converts the path into simple movement commands: Forward, Left, Right
- Estimates the total distance traveled based on the number of grid steps

## How It Works

This is not a machine learning model — it's a classic, well-known pathfinding pattern:

1. Find the lanes (open columns) between crop rows
2. Walk straight down the first lane
3. Turn to the next lane, walk back up
4. Repeat until every lane is covered

estimated_distance = number_of_steps × cell_spacing

I chose this approach because it's simple, explainable, and mirrors how real spraying robots plan coverage — without needing any training data or computer vision.

## How To Run

python farm_path_detector.py

## Notes

This is an early prototype focused on the path-planning logic itself, using a simplified, perfectly uniform grid instead of a real camera image. A real field isn't this uniform — rows curve, have gaps, and vary in spacing — so detecting the actual row layout from a photo (and detecting obstacles or people in real time) would need computer vision techniques I haven't learned yet. Those are possible future extensions, not part of this version.
