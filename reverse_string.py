from asyncflows import Action, BaseModel, Field

import aiohttp


class Inputs(BaseModel):
    input_string: str 
    word_index: int = Field(default=0, description="Index of the word to reverse")

class Outputs(BaseModel):
    reversed_string: str


class MyReverseString(Action[Inputs, Outputs]):
    name = "my_reverse_string"

    async def run(self, inputs: Inputs) -> Outputs:
        words = inputs.input_string.split()
        if 0 <= inputs.word_index < len(words):
            words[inputs.word_index] = words[inputs.word_index][::-1]
        return Outputs(
            reversed_string=' '.join(words)
        )
