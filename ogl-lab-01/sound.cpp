#include <iostream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_mixer.h>

int main()
{

    std::string currentFilePath = __FILE__;

    // Extract the directory path from the file path
    std::string directoryPath = currentFilePath.substr(0, currentFilePath.find_last_of("\\/"));

    // Form the full path to the "sample.wav" file
    std::string soundFilePath = directoryPath + "/sample.wav";

    if (SDL_Init(SDL_INIT_AUDIO) < 0)
    {
        std::cerr << "SDL initialization error: " << SDL_GetError() << std::endl;
        return 1;
    }

    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0)
    {
        std::cerr << "SDL_mixer initialization error: " << Mix_GetError() << std::endl;
        return 1;
    }

    Mix_Chunk *sound = Mix_LoadWAV(soundFilePath.c_str());
    if (sound == nullptr)
    {
        std::cerr << "Failed to load sound: " << Mix_GetError() << std::endl;
        return 1;
    }

    int channel = Mix_PlayChannel(-1, sound, 0);

    // You can add a delay here to let the sound play for a specific duration
    // while (Mix_Playing(channel) != 0 || Mix_Paused(channel) != 0) {
    //     SDL_Delay(50); // A short delay to yield CPU control
    //     SDL_PumpEvents(); // Pump the event loop to allow the OS to handle events
    // }

    SDL_Delay(5000);
    Mix_FreeChunk(sound); // Release the loaded sound

    Mix_CloseAudio();
    SDL_Quit();
    return 0;
}
