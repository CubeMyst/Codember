package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func decodeMessage(message string) string {
	wordCount := make(map[string]int)
	words := []string{}

	wordsList := strings.Fields(strings.ToLower(message))

	for _, word := range wordsList {
		if _, exists := wordCount[word]; !exists {
			words = append(words, word)
		}
		wordCount[word]++
	}

	result := ""
	for _, word := range words {
		result += word + fmt.Sprint(wordCount[word])
	}

	return result
}

func main() {
	messageBytes, err := ioutil.ReadFile("../data/Message_01.txt")
	if err != nil {
		fmt.Println("Error al leer el archivo: ", err)
		return
	}

	message := string(messageBytes)
	decodeMessage := decodeMessage(message)
	fmt.Println(decodeMessage)
}