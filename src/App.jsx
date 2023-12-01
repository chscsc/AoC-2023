import { SolutionProvider } from "./SolutionProvider";

import React from "react";
import { Button, Container, Card, Modal, Text, Textarea } from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";

export default function App() {
  const [input, setInput] = React.useState("");
  const solutionProvider = new SolutionProvider();

  const [part1Solution, setPart1Solution] = React.useState("");
  const [part2Solution, setPart2Solution] = React.useState("");

  const [opened, { open, close }] = useDisclosure(false);

  return (
    <div className="App">
      <Modal opened={opened} onClose={close} title={"Results"}>
        <b>Part 1</b>: {part1Solution}
        <br />
        <b>Part 2</b>: {part2Solution}
        <br />
      </Modal>

      <Textarea
        label="Input"
        description="Your input for whichever day you want to solve."
        placeholder="¯\_(ツ)_/¯"
        value={input}
        onChange={(e) => setInput(e.currentTarget.value)}
      />

      <br />
      <br />
      <hr />
      <br />
      <br />

      <Container>
        {solutionProvider.supportedDays().map((day) => (
          <Card withBorder padding="md" radius="md" shadow="sm">
            <Text fw={500}>Day {day}</Text>
            <Button
              variant="light"
              color="blue"
              fullWidth
              mt="md"
              radius="md"
              mb="sm"
              onClick={() => {
                const solution = solutionProvider.getSolution(day);

                const inputLines = input.split(/\r?\n/);

                setPart1Solution(solution.solve1(inputLines));
                setPart2Solution(solution.solve2(inputLines));

                open();
              }}
            >
              Solve
            </Button>
          </Card>
        ))}
      </Container>
    </div>
  );
}