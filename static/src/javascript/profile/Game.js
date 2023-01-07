import React, { Component } from 'react'
import { Media, Image, Content, Button, Icon, Form } from 'react-bulma-components';
import './Game.css'
import GenreList from '../genres/GenreList';

/* 
    module to display information about a game passed to it
    authors Riley Mathews
*/

class Game extends Component {

    state = {
        userGameId: "",
        isFavorited: false,
        isEditing: false
    }

    getGameUserId = function () {
        const thisGamesStats = this.props.userGamesStats.find(game => game.gbId === this.props.game.id)
        if (thisGamesStats !== undefined) {
            return thisGamesStats.id
        }
    }.bind(this)

    getGameFavorited = function () {
        const thisGamesStats = this.props.userGamesStats.find(game => game.gbId === this.props.game.id)
        if (thisGamesStats !== undefined) {
            return thisGamesStats.isFavorited
        }
    }

    gameOwned = function (owned) {
        if (owned) {
            return "owned"
        } else {
            return "not owned"
        }
    }

    removeGameById = function () {
        this.props.removeGameFromCollection(this.props.game.id)
    }.bind(this)

    render() {
        return (
            <Media>
                <Media.Item align='left'>
                    <Image src={this.props.game.image.icon_url} />
                </Media.Item>
                <Media.Item align='center'>
                    <Content>
                        <p className="inline">
                            <strong>{this.props.game.name}</strong>
                            {this.getGameFavorited() ? <Icon className="fas fa-star clickable" id={"game__toggle__favorite__" + this.getGameUserId()} onClick={this.props.toggleGameFavorite} /> : <Icon className="far fa-star clickable" id={"game__toggle__favorite__" + this.getGameUserId()} onClick={this.props.toggleGameFavorite} />}
                        </p>
                        <p>
                            {this.props.game.deck}
                        </p>
                    </Content>

                    <GenreList genres={this.props.game.genres} />
                </Media.Item >
                <Media.Item align='right'>
                    <Button remove onClick={this.removeGameById} />
                </Media.Item>
            </Media>
        )
    }
}

export default Game
